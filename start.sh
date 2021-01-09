#!/bin/bash
exec gunicorn -b 0.0.0.0:5000 "skade:create_app()"