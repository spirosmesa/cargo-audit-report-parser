# Cargo Audit Parser
A small python module using Python 3.9> that parses a JSON `cargo-audit` report.

It parses the report, and returns a list of dictionaries. 

It also offer methods for writting those results to a XLSX file.

# Usage Examples

# Method Documentation
Documentation on the methods can be found in the methods themselves,
within each Python file.

# Logging
Module logging can be configured by altering the contents of `__init__.py`.
The default logging configuration creates a (fresh) log file under 
`cargo_audit_parser\log_output`.