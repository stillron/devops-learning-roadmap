from flask import Flask, request
import time

app = Flask(__name__)

def check_app():
    return {"status": "ok"}

def check_database():
    time.sleep(0.01)
    return {"status": "ok", "connected": True}

check_functions = {
    'app': check_app,
    'db': check_database
}

@app.get("/health")
def get_health():
    available_checks = {'app', 'db'}
    params = request.args.get('checks')
    if params:
        requested_checks = set((params.split(',')))
        checks = available_checks.intersection(requested_checks)
    else:
        checks = available_checks

    response = {"checks": {}}
    for check_name in checks:
        func = check_functions[check_name]
        response['checks'][check_name] = func()
    
    is_healthy = True

    for v in response['checks'].values():
        print(v)
        if v.get('status') != 'ok':
            is_healthy = False
    
    if is_healthy:
        response['status'] = 'healthy'
    else:
        response['status'] = 'unhealthy'
    
    return response