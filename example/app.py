from rsk_mind.input import CSVInput

reader = CSVInput('in.csv')

reader.read()

print "Original Dataset"
print reader.header
print reader.rows


data = reader.transform()
print "Transformed Dataset"
