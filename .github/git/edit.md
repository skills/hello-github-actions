name: Go

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        go-version: [ '1.19', '1.20', '1.21.x' ]

    steps:
      - uses: actions/checkout@v4
      - name: Setup Go ${{ matrix.go-version }}
        uses: actions/setup-go@v5
        with:
          go-version: ${{ matrix.go-version }}
      # You can test your matrix by printing the current Go version
      - name: Display Go version
        run: go version
