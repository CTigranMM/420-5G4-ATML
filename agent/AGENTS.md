# AGENTS.md

## Project Overview
This repository contains a C++17 personal library management system (**Bibliothèque**) developed for coursework (`420-5G4-ATML`). It is an interactive console application for tracking books, library users, checkouts, and data persistence via plain text files.

## Project Structure
- `main.cpp`: Interactive CLI menu loop, argument parsing (`--data-dir` / `-d`).
- `book.h` / `book.cpp`: Book entity model (ISBN, title, author, year, checkout status, borrower tracking).
- `user.h` / `user.cpp`: User entity model (ID, name, email, list of borrowed book ISBNs).
- `library.h` / `library.cpp`: In-memory business logic and repository container managing books and users.
- `filemanager.h` / `filemanager.cpp`: Persistence layer reading/writing formatted text files (`books.txt`, `users.txt`).
- `data/`: Sample datasets (`books.txt`, `users.txt`).
- `CMakeLists.txt`: CMake build configuration targetting C++17 with strict warnings (`-Wall -Wextra -Wpedantic`).
- `.devcontainer/`: VS Code development container configuration (GCC / CMake).

## Build and Run

### Prerequisites
- C++17 compliant compiler (`g++`, `clang++`, or MSVC)
- CMake 3.21+
- Make / Ninja

### Build Instructions
```bash
mkdir build
cd build
cmake ..
make
```

### Execution
Run the compiled executable with optional path to dataset:
```bash
./bibliotheque -d ../data
```
Or with long-form argument:
```bash
./bibliotheque --data-dir ../data
```

## Conventions & Standards
- **Standard**: C++17 (`CXX_STANDARD 17`, extensions disabled).
- **Warnings**: Clean compile with `-Wall -Wextra -Wpedantic`.
- **Memory Management**: Modern C++ idioms using standard containers (`std::vector`) and smart pointers (`std::unique_ptr`). Raw pointers returned by lookup methods represent non-owning references.
- **Language**: User interface and console prompts are in French; identifiers, class members, and code logic are in English.
