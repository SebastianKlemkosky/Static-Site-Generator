class HTMLNode:
    def __init__(self, tag: str | None = None, value: str | None = None, children: list[HTMLNode] | None = None, props: dict | None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self) -> str:
        raise NotImplementedError()
    
    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        
        html = ""
        for prop in self.props:
            html += f" {prop}=\"{self.props[prop]}\""
        return html 
        
    def __repr__(self) -> str:
        return f"Tag: {self.tag}\n Value: {self.value}\n Children: {self.children}\n Props: {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str | None, props: dict | None = None) -> None:
        super().__init__(tag, value, None, props)
        
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("Missing value parameter")
        
        if self.tag is None:
            return self.value
        
  
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self) -> str:
            return f"Tag: {self.tag}\n Value: {self.value}\n Props: {self.props}"
        
        
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict | None = None) -> None:
        super().__init__(tag, None, children, props)
    
    
    
    def to_html(self) -> str:
            if self.tag is None:
                raise ValueError("Missing Tag parameter")
            if self.children is None:
                raise ValueError("Missing children parameter")
    
            children_html = ""
            for child in self.children:
                children_html += child.to_html()
                
            return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
