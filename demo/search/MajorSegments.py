def major_segments(s):
    """
    Perform major segmenting on a string.  Split the string by all of the major
    breaks, and return the set of everything found.  The breaks in this implementation
    are single characters, but in Splunk proper they can be multiple characters.
    A set is used because ordering doesn't matter, and duplicates are bad.
    """
    major_breaks = ' '
    last = -1
    results = set()

    # enumerate() will give us (0, s[0]), (1, s[1]), ...
    for idx, ch in enumerate(s):
        if ch in major_breaks:
            segment = s[last + 1:idx]
            results.add(segment)

            last = idx

    # The last character may not be a break so always capture
    # the last segment (which may end up being "", but yolo)
    segment = s[last + 1:]
    results.add(segment)

    return results


def segments(event):
    """Simple wrapper around major_segments / minor_segments"""
    results = set()
    for major in major_segments(event):
        for minor in major_segments(major):
            results.add(minor)
    return results


for term in segments('src_ip = 1.2.3.4'):
    print (term)
