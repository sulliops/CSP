import matplotlib.pyplot as plt
quantities = [62908, 26226, 32996, 14109, 18168]
labels= ['Management, professional,\n and related occupations', 'Service occupations', 'Sales and office occupations', 'Natural resources,\n construction and maintenance occupations', 'Production, transportation, and material moving occupations']
colors = ['pink', 'cyan', 'yellow', 'orange', 'green', 'magenta' ]
fig, ax = plt.subplots(1,1)
ax.pie(quantities, labels=labels, colors=colors, autopct='%.1f%%')
ax.set_aspect(1)
ax.set_title('Employed Persons by Occupation\n April 2019')
fig.show()