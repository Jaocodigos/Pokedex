from flask import Flask, render_template, session, flash, url_for, request, redirect
from app.resources import poke
import requests


@poke.route('/history', methods=['GET'])
def history():
    return render_template('/pages/history.html')
