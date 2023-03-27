import os
import sys
import typing

from opentelemetry.sdk.trace import Span
from opentelemetry.sdk.trace.export import SpanExporter, SpanExportResult


class PrintSpanExporter(SpanExporter):
    def __init__(
        self,
        out: typing.IO = sys.stdout,
        formatter: typing.Callable[[Span], str] = lambda span: span.to_json()
        + os.linesep,
    ):
        self.out = out
        self.formatter = formatter

    def format_span(self, span):
        time_taken = span.end_time - span.start_time
        return f"{span.name:<50}{time_taken:>8.1f} ms"

    def export(self, spans: typing.Sequence[Span]) -> SpanExportResult:
        for span in spans:
            self.out.write(self.format_span(span))
            self.out.write("\n")
        self.out.flush()
        return SpanExportResult.SUCCESS
