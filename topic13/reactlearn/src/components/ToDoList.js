export default function ToDoList(props){
    return(
        props.messages.map((message) =>
            <div className={"task_id_" + message.id + " task"}>
                <div className={"title"}>
                    <button id="delete-button" value={message.id} onClick={props.handleDelete} >Delete</button>
                    <h1>{message.title}</h1>
                </div>
                <div className={"description"}>
                    <p>{message.description}</p>
                </div>
            </div>
        )
    );

}