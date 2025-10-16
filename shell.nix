let
  pkgs = import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/nixos-unstable.tar.gz") { config = { }; };
in
  pkgs.mkShell {
    packages = with pkgs; [
      gcc
      uv

    ];

    env.LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      pkgs.stdenv.cc.cc
      pkgs.zlib
    ];
    # PYTHONPATH=".";
  }
