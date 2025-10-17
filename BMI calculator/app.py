from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    bmi_result = None
    category = None
    color_class = None # Used for CSS styling

    if request.method == 'POST':
        try:
            weight_kg = float(request.form.get('weight'))
            height_cm = float(request.form.get('height'))

            if weight_kg <= 0 or height_cm <= 0:
                raise ValueError("Weight and height must be positive numbers.")

            height_m = height_cm / 100

            bmi_result = weight_kg / (height_m ** 2)

            bmi_result = round(bmi_result, 2)


            if bmi_result < 16:
                category = "Malnourished"
                color_class = "malnourished"
            elif bmi_result < 18.5:
                category = "Underweight"
                color_class = "underweight"
            elif 18.5 <= bmi_result < 24.9:
                category = "Normal Weight"
                color_class = "normal"
            elif 25 <= bmi_result < 29.9:
                category = "Overweight"
                color_class = "overweight"
            else: 
                category = "Obese"
                color_class = "obese"

        except (ValueError, TypeError) as e:
            category = f"Error: Please enter valid numerical values. ({e})"
            bmi_result = "N/A"
            color_class = "error"

    return render_template(
        'index.html',
        bmi=bmi_result,
        category=category,
        color_class=color_class
    )

if __name__ == '__main__':
    app.run(debug=True)
