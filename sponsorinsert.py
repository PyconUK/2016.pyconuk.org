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

                   {'logo': '/img/logos/jpmc_logo.png',
                    'alt':  'JP Morgan',
                    'link': 'http://www.jpmorgan.com'},
                 ],]

SPONSORSILVER = [[{'logo': None,
                    'alt':  'Lyst',
                    'link': 'http://www.lyst.com'},
                  
                  {'logo': '/img/logos/gov.uk_logotype_crown.png',
                    'alt':  'Government Digital Service',
                    'link': 'https://gds.blog.gov.uk/'},
                  ],
                 [{'logo': '/img/logos/psf-logo.png',
                    'alt':  'Python Software Foundation',
                    'link': 'https://www.python.org/psf/'},
                  ],
                  ]


SPONSORBRONZE = [
                 [{'logo': '/img/logos/HPE_log_left_wht.png',
                    'alt':  'Hewlett Packard',
                    'link': 'https://www.hpe.com'},

                  {'logo': '/img/logos/potatoLogo.png',
                    'alt':  'Potato',
                    'link': 'http://www.potatolondon.com'},
                  ],
    
                 [{'logo': '/img/logos/logo_jetbrains.png',
                    'alt':  'JetBrains',
                    'link': 'http://www.jetbrains.com'},

                  {'logo': None,
                    'alt':  'Mosaic FM',
                    'link': 'http://www.mosaicfm.com'},
                  ],
                 [{'logo': '/img/logos/pythonanywherelogo-234x35.png',
                    'alt':  'PythonAnywhere',
                    'link': 'http://www.pythonanywhere.com'},

                  {'logo': None,
                    'alt':  'STX Next',
                    'link': 'www.stxnext.pl'},
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
