{{- range $key, $value := .Values.configs }}
{{ $key }} = {{ $value }}
{{- end }}
