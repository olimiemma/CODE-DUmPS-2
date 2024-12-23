#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:05:54 2024

@author: legend
"""

from flask import Flask, request, jsonify
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

app = Flask(__name__)

anthropic = Anthropic(api_key="YOUR_API_KEY")

@app.route('/get_response', methods=['POST'])
def get_response():
  data = request.get_json()
  prompt = data['prompt']
  completion = anthropic.completions.create(
      model="claude-2",
      max_tokens_to_sample=300,
      prompt=f"{HUMAN_PROMPT} {prompt} {AI_PROMPT}",
  )
  return jsonify({'response': completion.completion})

if __name__ == '__main__':
  app.run(debug=True)
