#!/usr/bin/env python3
import os, re, yaml, json

# Determine project root relative to script folder
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

tickets = []
for fname in sorted(os.listdir(os.path.join(BASE, 'tickets'))):
    if fname.endswith('.md'):
        fp = os.path.join(BASE, 'tickets', fname)
        fm = parse_frontmatter(fp)
        if fm:
            tickets.append({
                'key': fm.get('ticket_key', fname.replace('.md','')),
                'title': fm.get('title', ''),
                'status': fm.get('status', 'unknown'),
                'assignees': fm.get('assignees', {}),
                'sprint_code': fm.get('sprint_code', ''),
                'version': fm.get('version', ''),
                'parent_key': fm.get('parent_key', ''),
                'sub_tasks': fm.get('sub_tasks', []),
            })

status_count = {}
for t in tickets:
    s = t['status']
    status_count[s] = status_count.get(s, 0) + 1

print('=== STATUS COUNTS ===')
for s in sorted(status_count.keys()):
    print(f'{s}: {status_count[s]}')
print(f'TOTAL: {len(tickets)}')
print('===DETAILS===')
print(json.dumps(tickets, ensure_ascii=False, indent=2))
