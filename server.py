from flask import Flask, render_template
from database import Database
from rediscache import Cache


app = Flask(__name__)

# initialize the db
db = Database()

# initialize the redis cache
cache = Cache()


@app.route('/list')
def list_employees():

    def db_query():
        emps= cache.get_conn().get('listemp')

        if emps is None:
            emps= str(db.list_employees())
            print("employees list loaded from the db:", emps)

            # write into the cache
            cache.get_conn().set("listemp", str(emps))
        else:
            print("Obtained from the cache: ", str(emps))

        return eval(emps)

    # query db to get the list of the employees
    res = db_query()

    return render_template('employees.html', result=res, content_type='application/json')


if __name__ == "__main__":
    app.run()
