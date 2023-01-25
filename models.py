from flask import Flask, render_template, flash, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import sqlalchemy as sal
import pandas as pd
import random
import os
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm
from app import db

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.String(50), index=True, unique=True)
  email = db.Column(db.String(150), unique = True, index = True)
  password_hash = db.Column(db.String(150))
  joined_at = db.Column(db.DateTime(), default = datetime.utcnow, index = True)

  def set_password(self, password):
        self.password_hash = generate_password_hash(password)

  def check_password(self,password):
      return check_password_hash(self.password_hash,password)