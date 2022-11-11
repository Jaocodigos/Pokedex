from flask import Flask, render_template, session, flash, url_for, request, redirect
from app.resources import poke
import requests


@poke.route('/feedback', methods=['GET'])
def feedback():
    return render_template('/pages/feedback.html')
