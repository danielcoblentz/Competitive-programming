#!/usr/bin/env python3
"""
Problem 8 — Preprocessing (limited #ifdef / #else / #endif)
Read a source until a line with <EOF>. Then for each following line (sets of symbols),
output a comment with the symbols and the preprocessed text result.
"""

import sys


def preprocess(lines, defined):
    # lines: list of source lines (without trailing newlines)
    out = []
    # We'll use a stack to track whether current region is included.
    # Each stack element: (has_else, include_before_else, include_after_else)
    # Simpler: maintain include_stack of booleans indicating whether this level's text is active.
    # But due to #else we need to flip at that depth.
    include_stack = [True]
    # Also track for each depth whether the if condition was true (so we know which side to include)
    if_stack = []  # stores (cond_true, saw_else)

    for line in lines:
        if line.startswith("#ifdef "):
            sym = line[len("#ifdef "):]
            cond = sym in defined
            # when entering, the new include state is parent_include AND cond
            parent = include_stack[-1]
            include_stack.append(parent and cond)
            if_stack.append([cond, False])
        elif line == "#else":
            # flip the top include according to the original condition
            if not if_stack:
                # malformed per spec won't happen
                continue
            cond, saw_else = if_stack[-1]
            if saw_else:
                # per spec this should not happen
                pass
            if_stack[-1][1] = True
            parent = include_stack[-2]
            # include the else-branch when parent is True and cond is False
            include_stack[-1] = parent and (not cond)
        elif line == "#endif":
            if if_stack:
                if_stack.pop()
            if include_stack:
                include_stack.pop()
            if not include_stack:
                include_stack = [True]
        else:
            if include_stack[-1]:
                out.append(line)
    return out


def main():
    all_lines = [ln.rstrip('\n') for ln in sys.stdin]
    if not all_lines:
        return
    # find <EOF>
    try:
        idx = all_lines.index("<EOF>")
    except ValueError:
        return
    source = all_lines[:idx]
    cases = all_lines[idx+1:]

    # For each case line, parse symbols (split), create sorted list, and run preprocess
    first = True
    out_lines = []
    for case in cases:
        # each case line may be empty (no symbols)
        syms = [s for s in case.split() if s]
        syms_sorted = sorted(syms)
        # comment
        if syms_sorted:
            out_lines.append("/*" + "".join([s if i==0 else " " + s for i,s in enumerate(syms_sorted)]) + " */")
        else:
            out_lines.append("/* */")
        processed = preprocess(source, set(syms))
        out_lines.extend(processed)
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()
