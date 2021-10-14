from flask import Flask, request 
import platform


app = Flask(__name__)

@app.route('/')
def hello():
    system = platform.uname()
    platform1 = platform.machine()
    print(platform1)
    processor = platform.processor()
    table = """System: {} <br/>
                System Version: {} <br/>
                System Name: {} <br/>
                
                Processor: {} <br/><br/<br/>
                <a href='/user'>user<a/>""".format(system.system, system.version, system.node, processor)  
    return table

@app.route('/user')
def user():
    print(request.user_agent)
    return request.user_agent.string

