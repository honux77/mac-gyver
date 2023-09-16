import json

env = {}

def readEnv():
    # read env from env.json
    with open('env.json', 'r') as f:
        env = json.load(f)

def writeEnv():
    '''Writes the env to env.json'''
    with open('env.json', 'w') as f:
        json.dump(env, f, indent=4)

def getEnv(property):
    '''Returns the value of a property in the env'''
    return env[property]

def setEnv(property, value):
    '''Sets the value of a property in the env'''
    env[property] = value
    writeEnv()

def _clearEnv():
    '''Clears the env for test'''
    env = {}
    

# test code
if __name__ == '__main__':    
    setEnv('test', 't')
    print(getEnv('test'))
    writeEnv()
    _clearEnv()
    print(getEnv('test'))
    readEnv()
    print(getEnv('test'))
