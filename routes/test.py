from . import routes
from flask import Flask, render_template, request
@routes.route("/test")
def test():

    name = request.args.get('name')

    return name
    #return render_template('organisation.html')
