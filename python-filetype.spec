%define module filetype
%bcond tests 1

Name:		python-filetype
Version:	1.2.0
Release:	1
Summary:	Infer file type and MIME type of any file/buffer
License:	MIT
Group:		Development/Python
URL:		https://github.com/h2non/filetype.py
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:      noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
Small and dependency free Python package to infer file type and MIME type
checking the magic numbers signature of a file or buffer.

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
skiptests+="not test_guess_memoryview and not test_guess_extension_memoryview "
skiptests+="and not test_guess_mime_memoryview and not test_guess_zstd"
pytest tests/ --ignore tests/test_benchmark.py -k "$skiptests"
%endif

%files
%doc README.rst History.md examples
%license LICENSE
%{_bindir}/%{module}
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}-py%{pyver}.egg-info
