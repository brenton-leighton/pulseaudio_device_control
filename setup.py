from setuptools import setup

setup(name='pulseaudio_device_control',
    version='0.1',
    description='A simple script to control PulseAudio devices',
    keywords='pulseaudio',
    url='https://github.com/brenton-leighton/pulseaudio_device_control',
    author='Brenton Leighton',
    author_email='12228142+brenton-leighton@users.noreply.github.com',
    license='MIT',
    packages=['pulseaudio_device_control'],
    install_requires=[
        'pulsectl',
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'pulseaudio_device_control = pulseaudio_device_control.pulseaudio_device_control:main',
        ],
    },
)
