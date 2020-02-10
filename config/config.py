{{- range $key, $value := .Values.configs }}
{{ $key }} = {{ $value | quote }}
{{- end }}
