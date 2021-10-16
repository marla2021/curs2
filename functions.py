import json
from flask import Flask,request


DATA_PATH = "data/data.json"
COMMENTS = "data/comments.json"

def read_json(filename):
    with open(filename,'r', encoding="utf-8") as f:
        return json.load(f)


def get_commets_by_id(pk):
    all_comments = []
    for com in read_json(COMMENTS):
        if com["post_id"] == pk:
            all_comments.append(com)
    return all_comments


def get_posts():
    data=read_json(DATA_PATH)
    results =[]
    for post in data:
        comments = get_commets_by_id(post["pk"])
        new_post = post.copy()
        new_post["com_count"] = len(comments)
        results.append(new_post)
    return results

def get_post(postid):
    posts= read_json(DATA_PATH)
    for post in posts:
        if post["pk"] == postid:
            return post


def list_c(postid):
    comments=read_json(COMMENTS)
    posts= read_json(DATA_PATH)
    new_commets= []

    for comment in comments:
        if comment["post_id"] == postid:
            new_d = {}
            new_d["name"]=comment["commenter_name"]
            new_d["com"]=comment["comment"]
            new_commets.append(new_d)
    return new_commets


def search_user(username):
    posts = read_json(DATA_PATH)
    new_posts =[]
    for post in posts:
        if post["poster_name"]== username:
            new_posts.append(post)
    return new_posts
