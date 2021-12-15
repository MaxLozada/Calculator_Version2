from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value1'] == '':
            error = 'You must enter a value for value 1 and or value 2'
        else:
            flash('You successfully calculated')
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']

            # this will call the correct operation
            Calculator.calculate_numbers(operation, value1, value2)
            result = str(Calculator.get_calculation_last())
            return render_template('results.html', value1=value1, value2=value2, operation=operation,
                                   result=result)
        return render_template('calculator2.html', error=error)

    @staticmethod
    def get():
        return render_template('calculator2.html')
