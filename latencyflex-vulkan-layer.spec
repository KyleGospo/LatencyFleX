Name:       latencyflex-vulkan-layer
Version:    {{{ git_dir_version }}}
Release:    1%{?dist}
Summary:    Vendor agnostic latency reduction middleware
License:    Apache License 2.0
URL:        https://github.com/KyleGospo/LatencyFleX

BuildRequires:  git
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  vulkan-devel
BuildRequires:  vulkan-headers
BuildRequires:  vulkan-validation-layers-devel

%description
Vendor agnostic latency reduction middleware. An alternative to NVIDIA Reflex.

# Disable debug packages
%define debug_package %{nil}

%prep
git clone https://github.com/KyleGospo/LatencyFleX.git
cd LatencyFleX
git submodule update --init --recursive

%build
cd LatencyFleX/layer
meson build -Dprefix=%{_prefix}
ninja -C build

%install
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}
cp LatencyFleX/LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE
mkdir -p %{buildroot}%{_docdir}/%{name}
cp LatencyFleX/README.md %{buildroot}%{_docdir}/%{name}/README.md
cd LatencyFleX/layer
DESTDIR=%{buildroot} meson install -C build --skip-subprojects

%files
%license LICENSE
%doc README.md
%{_libdir}/liblatencyflex_layer.so
%{_datadir}/vulkan/implicit_layer.d/latencyflex.json

# Finally, changes from the latest release of your application are generated from
# your project's Git history. It will be empty until you make first annotated Git tag.
%changelog
{{{ git_dir_changelog }}}