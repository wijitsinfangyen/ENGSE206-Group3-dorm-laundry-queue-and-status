# Render the same geometry/text as the editable draw.io files, with Windows GDI+.
# No external packages. Run after build-diagrams.py from any working directory.
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing
$diagramDir = Join-Path (Split-Path $PSScriptRoot -Parent) 'diagrams'
$format = [System.Drawing.StringFormat]::new()
$format.Alignment = [System.Drawing.StringAlignment]::Center
$format.LineAlignment = [System.Drawing.StringAlignment]::Center
$font = [System.Drawing.Font]::new('Segoe UI',18,[System.Drawing.FontStyle]::Regular,[System.Drawing.GraphicsUnit]::Pixel)
$small = [System.Drawing.Font]::new('Segoe UI',17,[System.Drawing.FontStyle]::Regular,[System.Drawing.GraphicsUnit]::Pixel)
$title = [System.Drawing.Font]::new('Segoe UI',32,[System.Drawing.FontStyle]::Bold,[System.Drawing.GraphicsUnit]::Pixel)
$ink = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml('#0f172a'))
foreach ($name in @('context-after','container-after')) {
    $model = Get-Content -LiteralPath (Join-Path $diagramDir "$name.layout.json") -Raw | ConvertFrom-Json
    $bmp = [System.Drawing.Bitmap]::new([int]$model.width,[int]$model.height)
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.Clear([System.Drawing.Color]::White)
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
    $g.DrawString($model.title,$title,$ink,30,20)
    $g.DrawString($model.subtitle,$font,$ink,30,70)
    if ($model.boundary) {
        $r=$model.boundary
        $p=[System.Drawing.Pen]::new([System.Drawing.ColorTranslator]::FromHtml('#94a3b8'),2)
        $p.DashStyle=[System.Drawing.Drawing2D.DashStyle]::Dash
        $g.DrawRectangle($p,[int]$r[0],[int]$r[1],[int]$r[2],[int]$r[3])
        $g.DrawString('SYS-01  Dorm Laundry Queue and Status | Team responsibility',$font,$ink,([int]$r[0]+12),([int]$r[1]+12))
        $p.Dispose()
    }
    foreach ($e in $model.edges) {
        $p=[System.Drawing.Pen]::new([System.Drawing.ColorTranslator]::FromHtml('#475569'),2)
        $cap=[System.Drawing.Drawing2D.AdjustableArrowCap]::new(5,6,$true)
        $p.CustomStartCap=$cap; $p.CustomEndCap=$cap
        if ($e.dashed) { $p.DashStyle=[System.Drawing.Drawing2D.DashStyle]::Dash }
        [System.Drawing.PointF[]]$points=@($e.points | ForEach-Object { [System.Drawing.PointF]::new([single]$_[0],[single]$_[1]) })
        $g.DrawLines($p,$points)
        $p.Dispose(); $cap.Dispose()
    }
    foreach ($b in $model.boxes) {
        $fill='#dbeafe'; $stroke='#2563eb'
        if ($b.kind -eq 'actor') { $fill='#e2e8f0'; $stroke='#64748b' }
        if ($b.kind -eq 'external') { $fill='#fff7ed'; $stroke='#c2410c' }
        $brush=[System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml($fill))
        $p=[System.Drawing.Pen]::new([System.Drawing.ColorTranslator]::FromHtml($stroke),2)
        if ($b.kind -eq 'external') { $p.DashStyle=[System.Drawing.Drawing2D.DashStyle]::Dash }
        $rect=[System.Drawing.RectangleF]::new($b.x,$b.y,$b.w,$b.h)
        $g.FillRectangle($brush,$rect); $g.DrawRectangle($p,$b.x,$b.y,$b.w,$b.h)
        $textRect=[System.Drawing.RectangleF]::new(($b.x+8),($b.y+8),($b.w-16),($b.h-16))
        $g.DrawString($b.text,$font,$ink,$textRect,$format)
        $brush.Dispose(); $p.Dispose()
    }
    foreach ($e in $model.edges) {
        $r=$e.label
        $rect=[System.Drawing.RectangleF]::new($r[0],$r[1],$r[2],$r[3])
        $g.FillRectangle([System.Drawing.Brushes]::White,$rect)
        $g.DrawString($e.text,$small,$ink,$rect,$format)
    }
    $g.DrawString($model.footer,$small,$ink,[System.Drawing.RectangleF]::new(30,($model.height-70),($model.width-60),50))
    $bmp.Save((Join-Path $diagramDir "$name.png"),[System.Drawing.Imaging.ImageFormat]::Png)
    $g.Dispose(); $bmp.Dispose()
    Write-Output "Rendered $name.png"
}
$format.Dispose(); $font.Dispose(); $small.Dispose(); $title.Dispose(); $ink.Dispose()
