#!/bin/bash
manim lead_sheet_creator.py TableAnimation -pqh -r 2480,3508 && git add -A && git commit -m "create lead sheet" && git push
