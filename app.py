import decimal
from decimal import Decimal
from flask import Flask, jsonify
import logging

# Maximum nth fibonacci number
# The limit can be further increased if needed
LIMIT = 100_000

# Maximum number of digits
MAX_DIGITS = 30_000

app = Flask(__name__)
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s (%(name)s) [%(levelname)s]: %(message)s', datefmt='%Y-%m-%dT%H:%M:%S%z',
                    level=logging.INFO)


def fibonacci(n):
    logger.info(f'Calculating the {n}. factorial.')
    decimal.getcontext().prec = MAX_DIGITS
    a = Decimal(0)
    b = Decimal(1)

    # If the input is invalid
    if n < 0:
        raise ValueError('The value has to be a non-negative integer.')
    elif n == 0:
        return 0
    else:
        for i in range(n - 1):
            # Previous = Current
            # Current = Current + Previous
            a, b = b, a + b
        return b


# Define a route for the Fibonacci API
@app.get('/fibonacci/<int:n>')
def get_fibonacci(n):
    logger.info(f'User is looking for the {n}. factorial.')
    if n > LIMIT:
        return jsonify({'error': f'Limit of {LIMIT:,} exceeded.'})

    # Compute the nth Fibonacci number
    result = fibonacci(n)
    
    logger.debug(f'{n}. factorial is {result}')
    # Printing the input, the result and its length
    return jsonify({'input': n, 'fibonacci': str(result), 'fibonacci_length': len(str(result))})


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
