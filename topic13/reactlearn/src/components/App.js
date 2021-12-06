import React from "react";

class App extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            counter: 0, // читал я, что индексирование не самое лучшее решение
            title: '',
            description: '',
            messages: [],
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handlerChangeTitle = this.handlerChangeTitle.bind(this);
        this.handlerChangeDescription = this.handlerChangeDescription.bind(this);
        this.handleDelete = this.handleDelete.bind(this);
    }

    handleSubmit(event) {
        event.preventDefault();
        if (this.state.title.length > 0){
            this.state.messages.push({
                'id': this.state.counter,
                'title' : this.state.title,
                'description' : this.state.description,
            });
            this.setState({counter: this.state.counter+1});
        }
        else{
            this.setState({counter: this.state.counter});
            alert("Title must be not empty!");
        }
        this.setState({title: ''});
        this.setState({description: ''});
    }

    handlerChangeTitle(event) {
        if (event.target.value.length < 25) {
            this.setState({title: event.target.value});

        }
        else {
            alert("so big text  in title");
            this.setState({title: ''});
        }
        this.setState({counter: this.state.counter});

    }
    handlerChangeDescription(event) {
        this.setState({description: event.target.value});
    }

    handleDelete(event){
        for(let i =0; i< this.state.messages.length; i++){
            if(Number(this.state.messages[i].id) === Number(event.target.value)){
                this.state.messages.splice(i,1);
            }
        }
        this.setState({title: ''});
        this.setState({description: ''});
    }

    render() {
        return(
            <app>
                <header>
                    <h1>ToDo List</h1>
                </header>
                <main>
                    <div className="todos-list">
                        <ToDoList
                            messages={this.state.messages}
                            handleDelete={this.handleDelete}
                        />
                    </div>
                    <div className="todos-form">
                        <ToDoForm
                            handleSubmit={this.handleSubmit}
                            handlerChangeTitle={this.handlerChangeTitle}
                            handlerChangeDescription={this.handlerChangeDescription}
                            title={this.state.title}
                            description={this.state.description}
                        />
                    </div>
                </main>
                <footer>
                    <h1>Good luck</h1>
                </footer>
            </app>
        )
    }
}


function ToDoList(props){
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

function ToDoForm (props){
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