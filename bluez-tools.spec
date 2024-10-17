%define rev	662e

Name:			bluez-tools
Summary:		Command line tools for bluez (bluetooth stack for Linux)
Version:		0.1.38
Release:		0.%{rev}.3
Source0:		%{name}-%{version}-%{rev}.tar.gz
URL:			https://code.google.com/p/bluez-tools
License:		GPLv2
Group:			System/Kernel and hardware
Requires:		bluez >= 4.69
Requires:		obexd >= 0.30
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	readline-devel

%description
This is a GSoC'10 project to implement a new command line tools for 
bluez (bluetooth stack for linux). The project implemented in C and 
uses the D-Bus interface of bluez.

%prep
%setup -q -a 0 -n %{name}-%{version}-%{rev}

%build
%configure2_5x
%make

%install
make DESTDIR=%{buildroot} install

%files 
%doc README NEWS COPYING AUTHORS 
%{_bindir}/*
%{_mandir}/man1/bt-adapter.1*
%{_mandir}/man1/bt-agent.1*
%{_mandir}/man1/bt-audio.1*
%{_mandir}/man1/bt-device.1*
%{_mandir}/man1/bt-input.1*
%{_mandir}/man1/bt-monitor.1*
%{_mandir}/man1/bt-network.1*
%{_mandir}/man1/bt-obex.1*
%{_mandir}/man1/bt-serial.1*
