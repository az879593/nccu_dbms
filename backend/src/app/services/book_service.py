from ..models.book_model import db, Book

def create_book(data):
    """新增二手書資料"""
    # 驗證必要字段
    required_fields = ['書名', 'ISBN', '作者', '版本', '出版年份', '書本類別', '價格', '書況']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    try:
        # 構建書籍對象
        new_book = Book(
            書名=data['書名'],
            ISBN=data['ISBN'],
            作者=data['作者'],
            版本=data['版本'],
            出版年份=data['出版年份'],
            書本類別=data['書本類別'],
            價格=float(data['價格']),  # 確保價格為浮點數
            書況=data['書況']
        )
        # 將書籍添加到數據庫
        db.session.add(new_book)
        db.session.commit()
        return new_book
    except Exception as e:
        db.session.rollback()  # 回滾事務
        raise e
