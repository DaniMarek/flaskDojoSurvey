from flask import Flask, render_template, redirect, request, flash
app=Flask(__name__)
app.secret_key= 'toothpaste'

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
	content={
	"your_name": request.form['your_name'],
	"dojo_location": request.form['dojo_location'],
	"favorite_lang": request.form['favorite_lang'],
	"comment": request.form['comment']
	}
	if len(content['your_name']) < 1:
		flash("No name entered, please try again")
		return redirect('/')
	elif len(content['comment']) > 120:
		flash("Comment too long. Limit is 120 characters.")
		return redirect('/')
	else:
		return render_template('success.html', content = content)


app.run(debug=True)

