#! /usr/bin/env python

"""
This is a very simple script to convert a dict containing sponsor details
into a chunk of HTML. This chunk is then expected to be hand pasted into 
`content/sponsorship.md`. This is expected to be a low frequency use, and the
hacky approach is hopefully not that awful.  In short I doubt I will be generating 
the sponsor table often (only when we add a new sponsor).


"""

SPONSORGOLD = [[{'logo': '/img/logos/baml.gif',
                    'alt':  'Bank Of America',
                    'link': 'http://www.bankofamerica.com'},

                   {'logo': None,
                    'alt':  'JP Morgan',
                    'link': 'http://www.jpmorgan.com'},
                 ],]

SPONSORSILVER = [[{'logo': None,
                    'alt':  'Lyst',
                    'link': ''},

                  {'logo': None,
                    'alt':  'One',
                    'link': ''},
                  ],
                 [{'logo': None,
                    'alt':  'Two',
                    'link': ''},

                  {'logo': None,
                    'alt':  'Three',
                    'link': ''},
                  ],
                 [{'logo': None,
                    'alt':  'Four',
                    'link': ''},

                  {'logo': None,
                    'alt':  'Five',
                    'link': ''},
                  ]
                  ]


SPONSORBRONZE = [
                 [{'logo': None,
                    'alt':  'Six',
                    'link': ''},

                  {'logo': None,
                    'alt':  'Seven',
                    'link': ''},
                  ],
                 [{'logo': None,
                    'alt':  'Eight',
                    'link': ''},

                  {'logo': None,
                    'alt':  'Nine',
                    'link': ''},
                  ]
    
]

outertmpl = """<table>{0}</table>"""
dictmap = {'Gold': SPONSORGOLD,
           'Silver': SPONSORSILVER,
           'Bronze': SPONSORBRONZE
          }
html = '''We would like to thank all our sponsors whose generosity makes the conference possible.'''
for metal in ('Gold', 'Silver', 'Bronze'):
    html += '''\n\n### {0}\n\n<table>'''.format(metal)
    for row in dictmap[metal]:
        html += "<tr>"
        for sponsordata in row:
            # handle unknown icons
            if not sponsordata['logo']:
                sponsordata['logo'] = '/img/logos/placeholder.png'
                
            tmpl = '''<td>
                      <a href="{link}">
                      <img src="{logo}" alt="{alt}">
                      </a>
                      </td>'''
            html += tmpl.format(**sponsordata)
        html += "</tr>"
    html += "</table>"
print html
