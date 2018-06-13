from flask import Flask, render_template, redirect, request, session
#import the random module outside of importing flask
import random

app = Flask(__name__)

#secret key is needed to .GET 
app.secret_key = "454654966eg4swwrsfbgsf5b4s5f41g5sdfg5fs4hb5df4bh5f4nhgd5hsdmddjfjrhgjrhgrhgjrhgfie85890"

@app.route('/')
def index():
	#gets session to see if none. 
	#sets session gold_count to zero. always use .get to access a session!
	if session.get('gold_count') is None:
		session['gold_count'] = 0

	#gets session of the activities and checks to see if zero. 
	if session.get('activities') is None:
	#sets session of activites equal to empty list to append to. 
		session['activities'] = []
	return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
	#Use Session when you need your variables to be available to other pages the user might be accessing. 
	#You can get variables from the Request object only for the current and the previous form, so it is limited unlike Session.
	building = request.form['building']

	#uses hidden inputs name to see if it's the value of farm.
	#all inputs in the app have the same name "building" but different values to check against.
	if building == 'farm':
		#sets random number from range in the game level equal to a variable. 
		rand_num = random.randrange(10,20)
		session['gold_count'] += rand_num		#makes the variable number a string. Python cannot concatenate strings and numbers.
		session['activities'].append("Earned" + str(rand_num) + "gold from the" + building) 

	elif building == 'cave':
		rand_num = random.randrange(5,10)
		session['gold_count'] += rand_num		
		session['activities'].append("Earned" + str(rand_num) + "gold from the" + building)

	elif building == 'house':
		rand_num = random.randrange(2,5)
		session['gold_count'] += rand_num		
		session['activities'].append("Earned" + str(rand_num) + "gold from the" + building)

	elif building == 'casino':
		if session['gold_count'] >= 50:
			rand_num = random.randrange(-50, 51)
			#if the random number is negative, it'll be subtracted here, because it's a negative number. 
			session['gold_count'] += rand_num
			if rand_num < 0:
				session['activities'].append("You entered the" + " " + building + "and lost" + " "  + str(rand_num))
			if rand_num >= 0:
				session['activities'].append("You entered the" + " " +  building + "and won" + " " + str(rand_num))
 
	return redirect('/')


app.run(debug=True)