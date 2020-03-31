import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wasmtime",
    version="0.1.0",
    author="The Wasmtime Project Developers",
    author_email="hello@bytecodealliance.org",
    description="A WebAssembly runtime",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache-2.0 WITH LLVM-exception",
    url="https://github.com/bytecodealliance/wasmtime-py",
    packages=['wasmtime'],
    python_requires='>=2.7',
    test_suite="tests",
    install_requires=['setuptools >= 36'],
    extras_require={
        'testing': [
            'coverage',
            'pytest',
        ],
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Compilers',
        'Topic :: Software Development :: Interpreters',
        'Programming Language :: Rust',
    ]
)
