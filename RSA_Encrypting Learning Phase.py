
# coding: utf-8

# In[1]:

#gcd: Integer Integer -> Integer
#Returns the gcd of two integers, both of which are not 0

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


# In[2]:

gcd(49831,825579)


# In[3]:

#extended_euclid : Integer Integer -> (Integer, Integer)
#returns integers x, y such that ax + by = gcd(a,b)
#credit for theory: http://www.math.cmu.edu/~bkell/21110-2010s/extended-euclidean.html
def extended_euclid(a,b):
    table = {}
    return extended_euclid_helper(a,b,a,b, table = table)


# In[4]:

import math
#extended_euclid_helper : Integer Integer Integer Integer -> (Integer, Integer)
#ACCUMULATOR: c and d are the current numbers that are being used to find gcd
#ACCUMULATOR: _table_ is the set of equations that are being reused and manipulated to find the coeffeicients
def extended_euclid_helper(a,b,c,d, table):
    if d == 0:
        return table[c]
    r = c%d
    q = math.floor(c/d)
    if c == a and d == b:
        table[a] = (1,0)
        table[b] = (0,1)
        table[r] = (1,-q)
        return extended_euclid_helper(a,b,d,r, table)
    table[r] = (table[c][0] + -q*table[d][0],
                table[c][1] + -q*table[d][1])
    return extended_euclid_helper(a,b,d,r, table)
    


# In[5]:

extended_euclid(6735, 1343)


# In[6]:

gcd(1398,324)


# In[7]:

#inverse_mod: Integer Integer -> Integer
#finds the multiplicative inverse of x mod n _a_ such that ax mod n = 1
def inverse_mod(a,n):
    return int(extended_euclid(a,n)[0])


# In[8]:

#NEXT STEP: GENERATING PRIMES
import math
import random as rand
#is_prime: Number -> Boolean
#checks to see if a number is prime
#SOURCE: https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb
def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

#prime_generator: Number -> Number
#generates a random prime in the range [2,_n_]
#NOTE: This component was developed by me with the help of function above
def prime_generator(n):
    k = rand.randint(2,n+1)
    while (not(is_prime(k))):
        k = rand.randint(2,n+1)
    return k


# In[9]:

#message_converter: String -> [List-of Number]
#Converts a string of characters to chunks of ASCII representation
def message_converter(s):
    return list(map(ord,list(str(s))))


# In[10]:

#Generates random pair of public key and private key
def key_generator():
    p = prime_generator(10000000000)
    q = prime_generator(10000000000)
    n = p*q
    
    totient = (p-1)*(q-1)
    e = 65537
    private_key = int(inverse_mod(e,totient))
    public_key = (n,e)
    if private_key < 0:
        private_key += totient
    return (public_key, private_key)
    


# In[11]:

sid_keys = key_generator()


# In[12]:

sid_keys


# In[13]:

#rsa_encrypter: Number (Number, Number) -> Number
#encrypts a number with a given public key
def rsa_encrypter(m, key):
    return (pow(m, key[1], key[0]))
#encrypter: String, (Number, Number) -> [List-of Number]
#Encrypts all 'chunks' of a string
def encrypter(m,key):
    chunks = message_converter(m)
    return list(map((lambda x: (rsa_encrypter(x,key))), chunks))


# In[14]:

#rsa_decrypter: Number ((Number, Number), Number) -> String
#decrypts a message given a private key. Only decrypts message correctly if private key is the right one
def rsa_decrypter(encrypted, keys):
    return chr(pow(encrypted, keys[1], keys[0][0]))
#decrypter: [List-of Number] ((Number, Number), Number) -> String
#decrypts the encrypted chunks to retrieve original message
def decrypter(m, key):
    return ''.join(list(map((lambda x: (rsa_decrypter(x,key))), m)))


# In[15]:

encrypted_message = encrypter("a set of words that is complete in itself, typically containing a subject and predicate, conveying a statement, question, exclamation, or command, and consisting of a main clause and sometimes one or more subordinate clauses.", sid_keys[0])


# In[16]:

encrypted_message


# In[17]:

decrypter(encrypted_message,sid_keys)


# In[22]:

import dash
import dash_core_components as dcc
import dash_html_components as html


# In[23]:

app = dash.Dash()


# In[24]:

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='Graph1',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])


# In[ ]:



