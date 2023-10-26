# Use regular expression to split the string
result = re.split(r",(?=(?:[^']*'[^']*')*[^']*$)", text)

# Remove single quotes from the elements
result = [s.strip("'") for s in result]
