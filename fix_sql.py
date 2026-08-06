import re

def fix_sql_strings(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all cursor.execute(''' ... ''') and replace with cursor.execute(" ... ")
    # But carefully since SQL can span multiple lines.
    # Actually, we can just replace ''' with """ - wait, if Pyrefly triggers on multiline strings entirely, we should convert them to single line or concatenated strings.
    
    def replacer(match):
        sql = match.group(1)
        # remove leading/trailing newlines
        sql = sql.strip()
        # split by newline and build concatenated string
        lines = sql.split('\n')
        # format: ("line1 " "line2")
        formatted = "(\n"
        for line in lines:
            line = line.strip()
            if line:
                # escape double quotes if any
                line = line.replace('"', '\\"')
                formatted += f'            "{line} "\n'
        formatted += "        )"
        return f'cursor.execute({formatted}'

    # regex to find cursor.execute(''' ... ''')
    new_content = re.sub(r"cursor\.execute\('''(.*?)'''", replacer, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Fixed.")

if __name__ == '__main__':
    fix_sql_strings('app.py')
