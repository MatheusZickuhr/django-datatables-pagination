from distutils.core import setup

setup(
    name='django-datatables-pagination',
    packages=['dt_pagination'],
    version='0.1',
    license='MIT',
    description='A Django ListView integration with datatables library.',
    author='Matheus Zickuhr',
    author_email='matheuszickuhr97@gmail.com',
    url='https://github.com/MatheusZickuhr/django-datatables-pagination',
    keywords=['django', 'datatables', 'pagination'],
    install_requires=['django'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ],
)
