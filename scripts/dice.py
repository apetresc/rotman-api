from flask import Flask, request, jsonify
import json
import random

app = Flask("dice")


def roll(n, d):
  return sum([random.randint(1, d) for _ in range(n)])


@app.route('/roll')
def roll_method():
  return jsonify({
    "total": roll(int(request.args["n"]), int(request.args["d"]))
  })
