from MyApp import app,db
from flask import Flask ,render_template,url_for,flash,session,request,redirect 

@app.route("/")
def home():
    if request.method =='POST':
        user = User.query.filter_by(email= request.form['email']).first()
        if user and bcrypt.check_password_hash(user.password, request.form['password']):
            session['email'] = request.form['email']
            flash(f'Welcome, you are logged in','success')
            return redirect(request.args.get('next') or url_for('login'))

        else:
            flash(f'Wrong password try  again', 'danger')
         
    
    return render_template('login.html', title ="Login page" )

@app.route("/signUp", methods=['GET', 'POST'])
def  signup():
    if request.method == 'POST':
        hash_password = bcrypt.generate.password_hash(request.form['password'])
      
        
        confirm=request.form['confirm']
            
        signp = Signup(name=request.form['name'],username=request.form['username'],email=request.form['email'],password=hash_password)

        db.session.add(signp)
        db.session.commit()
        flash(f"Thank you for subscribing...",'success')
        return redirect(url_for('index'))
    return render_template('signup.html'  , title ="Registeration page" )

@app.route("/home")
def index():
    
    return render_template('dashboard.html')

@app.route('/addproduct', methods=['POST','GET'])
def addProduct(): 
    product = Product.query.all()
    if request.method=="POST":
        Product_name = request.form.get('name')
        price= request.form.get('price')
        quality= request.form.get('discount')
        
        addpro = Product(Product_name=Product_name, price=price,quality=quality )
        db.session.add(addpro)
        db.session.commit()
        flash(f'The product {name } was added to your database','success')
        return redirect(url_for('index'), product=Product)



    return render_template('dashboad.html' )
    