export default function ToDoForm (props){
    return (
        <form onSubmit={props.handleSubmit}>
            <label>
                Title:
                <input type="text" value={props.title} onChange={props.handlerChangeTitle}/>
            </label>
            <label>
                Description:
                <textarea value={props.description} onChange={props.handlerChangeDescription} />
            </label>
            <input type="submit" value="New ToDo"/>
        </form>
    )
}