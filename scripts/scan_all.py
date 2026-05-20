#!/usr/bin/env python3
"""Scan tickets, requirements, sprints, versions for dashboard stats."""
import os, re, yaml, json, glob

# Determine project root relative to script folder (parent of scripts/)
script_dir = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(script_dir)

def parse_frontmatter(filepath):
    with open(filepath) as f:
        content = f.read()
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except:
        return None

# --- TICKETS ---
tickets = []
for fname in sorted(os.listdir(os.path.join(BASE, 'tickets'))):
    if fname.endswith('.md'):
        fp = os.path.join(BASE, 'tickets', fname)
        fm = parse_frontmatter(fp)
        if fm:
            tickets.append({
                'key': fm.get('ticket_key', ''),
                'title': fm.get('title', ''),
                'status': fm.get('status', 'unknown'),
                'assignees': fm.get('assignees', {}),
                'sprint_code': fm.get('sprint_code', ''),
                'version': fm.get('version', ''),
            })

# Status counts
status_count = {}
for t in tickets:
    s = t['status']
    status_count[s] = status_count.get(s, 0) + 1

# Assignee grouping (by dev_app, dev_backend, dev_web)
from collections import defaultdict
assignee_tickets = defaultdict(list)
for t in tickets:
    a = t.get('assignees', {})
    for role in ['dev_app', 'dev_web', 'dev_backend']:
        name = a.get(role)
        if name and name != 'null':
            assignee_tickets[name].append({'key': t['key'], 'title': t['title'], 'status': t['status']})

# --- REQUIREMENTS ---
reqs = []
req_dir = os.path.join(BASE, 'requirements')
if os.path.isdir(req_dir):
    for fname in sorted(os.listdir(req_dir)):
        if fname.endswith('.md'):
            fp = os.path.join(req_dir, fname)
            fm = parse_frontmatter(fp)
            if fm:
                reqs.append({
                    'id': fm.get('requirement_id', fname.replace('.md','')),
                    'title': fm.get('title', ''),
                    'status': fm.get('status', 'unknown'),
                    'related_tickets': fm.get('related_tickets', []),
                })

# --- VERSIONS ---
versions = []
ver_dir = os.path.join(BASE, 'versions')
if os.path.isdir(ver_dir):
    for fname in sorted(os.listdir(ver_dir)):
        if fname.endswith('.md'):
            fp = os.path.join(ver_dir, fname)
            fm = parse_frontmatter(fp)
            if fm:
                versions.append({
                    'version': fm.get('version', fname.replace('.md','')),
                    'status': fm.get('status', 'unknown'),
                    'tickets': fm.get('tickets', []),
                    'release_date': str(fm.get('release_date', '')) if fm.get('release_date') else '',
                })

# --- FEEDBACKS ---
feedbacks = []
fb_dir = os.path.join(BASE, 'feedbacks')
if os.path.isdir(fb_dir):
    for fname in sorted(os.listdir(fb_dir)):
        if fname.endswith('.md'):
            fp = os.path.join(fb_dir, fname)
            fm = parse_frontmatter(fp)
            if fm:
                feedbacks.append({
                    'id': fm.get('fb_id', fname.replace('.md','')),
                    'title': fm.get('title', ''),
                    'type': fm.get('fb_type', ''),
                    'channel': fm.get('channel', ''),
                    'group': fm.get('fb_group', ''),
                    'handler': fm.get('handler', ''),
                    'collaborators': fm.get('collaborators', []),
                    'progress': fm.get('progress', ''),
                    'result': fm.get('result', ''),
                    'updates': fm.get('updates', []),
                    'related_tickets': fm.get('related_tickets', []),
                })

# --- OUTPUT ---
print("===STATUS_COUNTS===")
print(json.dumps(status_count))

print("===ASSIGNEE_TICKETS===")
# Group by assignee
for name, tix in sorted(assignee_tickets.items()):
    print(f"--- {name} ---")
    for t in tix:
        print(f"  {t['key']}: [{t['status']}] {t['title']}")

print("===REQUIREMENTS===")
print(json.dumps(reqs, ensure_ascii=False, indent=2))

print("===FEEDBACKS===")
print(json.dumps(feedbacks, ensure_ascii=False, indent=2))

print("===VERSIONS===")
print(json.dumps(versions, ensure_ascii=False, indent=2))

print("===TOTAL_TICKETS===")
print(len(tickets))
