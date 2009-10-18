%define tarname amqplib

Name:           py-amqplib
BuildRequires:  python-devel
BuildArch:      noarch
Summary:        AMQP Library for Python
Version:        0.6.1
Release:        1
Source0:        %{tarname}-%{version}.tgz
License:        Public Domain, LGPL
Group:          Development/Libraries/Python
URL:            http://py-amqplib.googlecode.com
Autoreqprov:    on
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n )
BuildRequires:  python-devel

%description
 py-amqplib is a client Python library for working with AMQP message
  systems.  It has been tested under RabbitMQ and Apache QPID.

    amqp.client             (Full consumer / producer interface)

Authors:
--------
   Source:
     Barry Pederson (barry.pederson AT ???)
   RPM:
     Randy Secrist (randy.secrist AT gmail.com)

%prep
%setup -n amqplib-%{version}

%build
export CFLAGS="$RPM_OPT_FLAGS"
python setup.py build

%install
python setup.py install --optimize=1 --prefix=%{_prefix} --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Sun Oct 18 2009 Randy Secrist <randy.secrist@gmail.com> 0.6.1-1
- Packaged up latest TAR from google code.
