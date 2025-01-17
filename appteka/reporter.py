# appteka - helpers collection

# Copyright (C) 2018-2025 Aleksandr Popov

# This program is free software: you can redistribute it and/or modify
# it under the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Lesser GNU General Public License for more details.

# You should have received a copy of the Lesser GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Classes for building simple reports with text and pictures."""

import os

HTML_PIC_WIDTH = 800


class Reporter:
    """Base class for reporter."""

    def __init__(self):
        self._report = ""

    def begin(self):
        """Start the building of report. Some actions may be needed
        fisrt. Make it here."""

    def end(self):
        """Some actions in the end of the process of building."""

    def add_header(self, header_text, level=1):
        """Add header.

        Parameters
        ----------
        header_text : str
            Text of header.
        level : int
            Level of header.
        """
        raise NotImplementedError

    def add_pic(self, path):
        """Add image to report.

        Parameters
        ----------
        pic_path : str
            Name of image file.
        """
        raise NotImplementedError

    def add_text(self, text):
        """Add plain text to report.

        Parameters
        ----------
        text : str
            Text
        """
        raise NotImplementedError

    def report(self, file_name, encoding):
        """Save report."""
        raise NotImplementedError


class HtmlReporter(Reporter):
    """HTML reporter."""

    def begin(self):
        """Create the head of html-document and start the body."""
        self._report += "<html>\n"
        self._report += "<head><Meta charset='UTF-8'/></head>\n"
        self._report += "<body>\n"

    def end(self):
        """Put close tags to the end of HTML-document."""
        self._report += "</body>\n"
        self._report += "</html>\n"

    def add_header(self, header_text, level=1):
        """Add header.

        Parameters
        ----------
        header_text : str
            Text of header.
        level : int
            Level of header.
        """
        self._report += f'<h{level}>{header_text}</h{level}>\n'

    def add_pic(self, path):
        """Add image to report.

        Parameters
        ----------
        pic_path : str
            Name of image file.
        """
        self._report += f'<img src=\'{path}\' width=\'{HTML_PIC_WIDTH}\'>\n'

    def add_text(self, text):
        """Add plain text to report.

        Parameters
        ----------
        text : str
            Text
        """
        self._report += f'<pre>{text}</pre>\n'

    def report(self, file_name, encoding='utf-8'):
        """Save report."""
        with open(file_name, "w", encoding=encoding) as buf:
            buf.write(self._report)


class LatexReporter(Reporter):
    """LaTeX reporter."""

    def add_header(self, header_text, level=1):
        """Add header.

        Parameters
        ----------
        header_text : str
            Text of header.
        level : int
            Level of header.
        """
        if level == 1:
            self._report += "\n\\HeaderCommandOne{" + header_text + "}\n"
        elif level == 2:
            self._report += "\n\\HeaderCommandTwo{" + header_text + "}\n"
        elif level == 3:
            self._report += "\n\\HeaderCommandThree{" + header_text + "}\n"
        else:
            self._report += "\n{" + header_text + "}\n"

    def add_pic(self, path):
        """Add image to report.

        Parameters
        ----------
        pic_path : str
            Name of image file.
        """
        self._report += "\n\\InsertPicCommand{"
        self._report += os.path.abspath(os.path.expanduser(path))
        self._report += "}\n"

    def add_text(self, text):
        """Add plain text to report.

        Parameters
        ----------
        text : str
            Text
        """
        self._report += "\n\\TraceTextCommand{" + text + "}\n"

    def report(self, file_name, encoding='utf-8'):
        """Save report."""
        with open(file_name, "w", encoding=encoding) as buf:
            buf.write(self._report)
