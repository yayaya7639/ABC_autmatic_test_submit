# ユーザーのフィードバックに基づいてスクリプトを修正し、プレゼンテーションを再作成

# 新しいプレゼンテーションを作成
prs = Presentation()

# スライドのサイズを16:9に設定
prs.slide_width = Inches(13.33)
prs.slide_height = Inches(7.5)

# スライドを追加（タイトルやテンプレートは使用しない）
slide = prs.slides.add_slide(prs.slide_layouts[6])

# スライドタイトル用のテキストボックスを追加（左揃え）
title_shape = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), prs.slide_width - Inches(1), Inches(1))
title_text_frame = title_shape.text_frame
title_text_frame.text = "タイトルを入力"  # タイトルのテキスト
for paragraph in title_text_frame.paragraphs:
    paragraph.alignment = PP_ALIGN.LEFT  # 左揃え
    for run in paragraph.runs:
        run.font.bold = True

# 「見出し」用のテキストボックスを追加（中央揃え）
header_shape = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), prs.slide_width - Inches(1), Inches(1))
header_text_frame = header_shape.text_frame
header_text_frame.text = "見出し"  # 見出しのテキスト
for paragraph in header_text_frame.paragraphs:
    paragraph.alignment = PP_ALIGN.CENTER  # 中央揃え
    for run in paragraph.runs:
        run.font.bold = True

# 見出し下の線を挿入
line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(2.6), prs.slide_width - Inches(1), Pt(2))
fill = line.fill
fill.solid()
fill.fore_color.rgb = RGBColor(0, 0, 0)  # 黒色
line.shadow.inherit = False

# セクションと箇条書き用のテキストボックスを複数追加
for i in range(3):
    # セクションタイトル
    section_shape = slide.shapes.add_textbox(Inches(0.5), Inches(3) + Inches(1.5) * i, Inches(2), Inches(0.5))
    section_text_frame = section_shape.text_frame
    section_text_frame.text = f"セクション{i+1}"
    for paragraph in section_text_frame.paragraphs:
        paragraph.alignment = PP_ALIGN.CENTER  # 中央揃え

    # 箇条書き用のテキストボックス
    content_shape = slide.shapes.add_textbox(Inches(3), Inches(3) + Inches(1.5) * i, prs.slide_width - Inches(3.5), Inches(1))
    content_text_frame = content_shape.text_frame
    content_text_frame.text = "• 箇条書き1"
    p = content_text_frame.add_paragraph()
    p.text = "• 箇条書き2"
    for paragraph in content_text_frame.paragraphs:
        paragraph.level = 0  # 箇条書きレベルの設定
        paragraph.alignment = PP_ALIGN.LEFT

# ファイルを保存
prs.save('/mnt/data/adjusted_custom_slide_layout.pptx')
