import fileinput

in_header=False
header_line_count = 0
for line in fileinput.input():
    line = line.strip('\n')
    if line == "---":
        line = "+++"
        if header_line_count == 0:
            in_header = True
        else:
            in_header = False
        print(line)
        header_line_count += 1

    elif in_header:
        if line.startswith('title') or line.startswith('date'):
            fields = line.replace('"', '').replace("'",'').split(':')
            key = fields[0]
            val = ':'.join(fields[1:])
            if key == "date":
                val = val.split('T')[0]
            line = f'{key} = "{val.strip()}"'
            print(line)
    else:
        line = line.replace('{{ site.baseurl }}/assets', '')
        print(line)

